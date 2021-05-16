$(document).ready(function () {

    let work = $('#work'); // select для выбора - группа или преподаватель
    let facultyStud = $('#facultyStud'); // select - выбор факультета группы
    let facultyTeach = $('#facultyTeach'); // select - выбор факультета преподавателя
    let departmentStud = $('#departmentStud'); // select - выбор кафедры группы
    let departmentTeach = $('#departmentTeach'); // select - выбор кафедры преподавателя
    let course = $('#course'); // select - выбор курса группы
    let group = $('#group'); // select - выбор группы
    let teacher = $('#teacher'); // select - выбор преподавателя
    let formStud = $('#formStud'); // form для выбора группы
    let formTeach = $('#formTeach'); // form для выбора преподавателя
    let selLang = $('#language'); // select для выбора языка

    let current_url = window.location.href; // текущий полный url
    let word_department = 'department=';
    let word_group = 'group=';
    let word_teacher = 'teacher=';
    let ru = '/ru/';
    let ua = '/ua/';
    let en = '/en/';

    selLang.on('change', function () {

        let cur_lang;

        if (current_url.includes(ru))
        {
            cur_lang = ru;
        }
        else if (current_url.includes(ua))
        {
            cur_lang = ua;
        }
        else {
            cur_lang = en;
        }

        // console.log(current_url);
        // console.log(cur_lang);
        // console.log($(this).val());
        let place_locale = current_url.indexOf(cur_lang);
        console.log(place_locale);
        let test = current_url.slice(0, place_locale);
        if (place_locale + cur_lang.length === current_url.length)
        {
            window.location=test + "/" + $(this).val() + "/";
        }
        else {
            let test1 = current_url.slice(place_locale + cur_lang.length, current_url.length);
            console.log(test1);
            window.location=test + "/" + $(this).val() + "/" + test1;
        }

    });

    function genericColor() {
        let rgb = [];
        let r = Math.floor((Math.random() * 255) + 1);
        let g = Math.floor((Math.random() * 255) + 1);
        let b = Math.floor((Math.random() * 255) + 1);
        rgb[0] = r;
        rgb[1] = g;
        rgb[2] = b;
        return rgb;
    } // создает случайный цвет

    function listRGBA(countObj) {
        let listFull = [];
        let listBg = [];
        let listBd = [];
        for(let i=0; i<countObj; i++)
        {
            let rgb = genericColor();
            listBg[i] = `rgba(${rgb[0]}, ${rgb[1]}, ${rgb[2]}, ${0.5})`;
            listBd[i] = `rgba(${rgb[0]}, ${rgb[1]}, ${rgb[2]}, ${1})`;
        }
        listFull[0] = listBg;
        listFull[1] = listBd;
        return listFull;
    } // создает массив цветов для бэкграунда и границ графиков

    function buildChart(container, type, labels, label, data, bgColor, bColor, options) {
        if (options === true)
        {
            let myChart = new Chart(container, {
                type: type,
                data: {
                    labels: labels,
                    datasets: [{
                        label: label,  // Locale
                        data: data,
                        backgroundColor: bgColor,
                        borderColor: bColor,
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    }
                }
            }); // объект для построения графика
        }
        else {
            let myChart = new Chart(container, {
                type: type,
                data: {
                    labels: labels,
                    datasets: [{
                        label: label,  // Locale
                        data: data,
                        backgroundColor: bgColor,
                        borderColor: bColor,
                        borderWidth: 1
                    }]
                }
            }); // объект для построения графика
        }
    }

    if (current_url.includes(word_department)) // проверка, есть ли кафедра в url
    {

        let data = {};

        if (current_url.includes(word_teacher)) // проверка, есть ли преподаватель в url
        {
            console.log(word_teacher);

            let start_symbol_t = current_url.indexOf(word_teacher) + word_teacher.length;
            let id_teacher = current_url.slice(start_symbol_t, start_symbol_t+1);
            console.log(id_teacher);

            data.id_teacher = id_teacher;
            data.current_language = selLang.val();

            $.ajax({
                url: '/local_charts_teacher/',
                type: 'GET',
                data: data,
                cache: true,
                success: function (data) {
                    let parseData = JSON.parse(data);
                    console.log(data);
                    console.log(parseData);
                    let col1 = listRGBA(parseData['numberHall'].length);
                    let col2 = listRGBA(parseData['numberLesson'].length);
                    let col3 = listRGBA(parseData['typeSubject'].length);
                    let ctx1 = document.getElementById('myChartLocalHall').getContext('2d');
                    let ctx2 = document.getElementById('myChartLocalLesson').getContext('2d');
                    let ctx3 = document.getElementById('myChartLocalTypeLesson').getContext('2d');
                    buildChart(ctx1, 'bar', parseData['numberHall'], parseData['nameLabel'][0], parseData['countHallNH'], col1[0], col1[1], true);
                    buildChart(ctx2, 'bar', parseData['numberLesson'], parseData['nameLabel'][1], parseData['countLessonNL'], col2[0], col2[1], true);
                    buildChart(ctx3, 'pie', parseData['typeSubject'], parseData['nameLabel'][2], parseData['countLessonTS'], col3[0], col3[1], false);
                },
                error: function () {
                    alert("Ошибка");
                }
            }); //запрос на сервер для предоставления информации для графика
        }
        else {
            console.log('student');

            let start_symbol_d = current_url.indexOf(word_department) + word_department.length;
            let id_department = current_url.slice(start_symbol_d, start_symbol_d+1);
            console.log(id_department);

            let start_symbol_g = current_url.indexOf(word_group) + word_group.length;
            let id_group = current_url.slice(start_symbol_g, start_symbol_g+1);
            console.log(id_group);

            data.id_department = id_department;
            data.id_group = id_group;
            data.current_language = selLang.val();

            $.ajax({
                url: '/local_charts_group/',
                type: 'GET',
                data: data,
                cache: true,
                success: function (data) {
                    let parseData = JSON.parse(data);
                    console.log(data);
                    console.log(parseData);
                    let col1 = listRGBA(parseData['numberHall'].length);
                    let col2 = listRGBA(parseData['numberLesson'].length);
                    let col3 = listRGBA(parseData['typeSubject'].length);
                    let ctx1 = document.getElementById('myChartLocalHall').getContext('2d');
                    let ctx2 = document.getElementById('myChartLocalLesson').getContext('2d');
                    let ctx3 = document.getElementById('myChartLocalTypeLesson').getContext('2d');
                    buildChart(ctx1, 'bar', parseData['numberHall'], parseData['nameLabel'][0], parseData['countHallNH'], col1[0], col1[1], true);
                    buildChart(ctx2, 'bar', parseData['numberLesson'], parseData['nameLabel'][1], parseData['countLessonNL'], col2[0], col2[1], true);
                    buildChart(ctx3, 'pie', parseData['typeSubject'], parseData['nameLabel'][2], parseData['countLessonTS'], col3[0], col3[1], false);
                },
                error: function () {
                    alert("Ошибка");
                }
            }); //запрос на сервер для предоставления информации для графика
        }
    }
    else {
        console.log('void')
    }

    // new Chart(document.getElementById("chartjs-4"), {
    //     "type":"doughnut",
    //     "data":{
    //         "labels":["Red","Blue","Yellow"],
    //         "datasets": [{
    //             "label":"My First Dataset",
    //             "data":[300,50,100],
    //             "backgroundColor":[
    //                 "rgb(255, 99, 132)",
    //                 "rgb(54, 162, 235)",
    //                 "rgb(255, 205, 86)"]
    //         }]
    //     }
    // });

    work.on('change', function () {

        if(work.val() === "1")
        {
            formStud.show();
            formTeach.hide();
        }
        else if(work.val() === "2")
        {
            formTeach.show();
            formStud.hide();
        }
        else {
            formStud.hide();
            formTeach.hide();
        }

    }); // выбор, какую форму показывать: для поиска преподавателя или поиска группы

    formStud.submit(function (e) {
        console.log(facultyStud.val());
        if (facultyStud.val() === "0" || departmentStud.val() === "0" || course.val() === "0" || group.val() === "0")
        {
            e.preventDefault();
            if (selLang.val() === ru)
            {
                alert('Вы не ввели факультет/кафедру/курс/группу')  // Locale
            }
            else if (selLang.val() === ua)
            {
                alert('Ви не ввели факультет/кафедру/курс/групу')  // Locale
            }
            else {
                alert('You have not entered a faculty / department / course / group')  // Locale
            }
        }
    }); // обработка ввода не всех данных для поиска группы

    formTeach.submit(function (e) {
        console.log(facultyTeach.val());
        if (facultyTeach.val() === "0" || departmentTeach.val() === "0" || teacher.val() === "0")
        {
            e.preventDefault();
            if (selLang.val() === ru)
            {
                alert('Вы не ввели факультет/кафедру/учителя')  // Locale
            }
            else if (selLang.val() === ua)
            {
                alert('Ви не ввели факультет/кафедру/вчителя')  // Locale
            }
            else {
                alert('You have not entered a faculty/department/teacher')  // Locale
            }

        }
    }); // обработка ввода не всех данных для поиска преподавателя

    facultyStud.on('change', function () {

        let countDep = $(departmentStud).children('option').length;

        console.log(countDep);

        if(countDep > 1)
        {
            departmentStud.empty();
            departmentStud.append('<option value="0" selected>-----</option>')
        }

        console.log($(this).val());

        let data_fac = {};
        data_fac.id_faculty = $(this).val();
        data_fac.current_language = selLang.val();

        $.ajax({
            url: '/faculty/',
            type: 'GET',
            data: data_fac,
            cache: true,
            success: function (data) {
                let parseData = JSON.parse(data);
                for (let key in parseData) {
                    departmentStud.append('<option value="' + key + '">' + parseData[key] + '</option>')
                }
            },
            error: function () {
            }
        })

    }); // обработка изменения факультета группы

    course.on('change', function () {

        let countGrp = $(group).children('option').length;

        console.log(countGrp);

        if(countGrp > 1)
        {
            group.empty();
            group.append('<option value="0" selected>-----</option>')
        }

        console.log($(this).val());

        let data_cou = {};
        data_cou.id_course = $(this).val();

        $.ajax({
            url: '/course/',
            type: 'GET',
            data: data_cou,
            cache: true,
            success: function (data) {
                let parseData = JSON.parse(data);
                for (let key in parseData) {
                    group.append('<option value="' + key + '">' + parseData[key] + '</option>')
                }
            },
            error: function () {
            }
        })

    }); // обработка изменения курса группы

    facultyTeach.on('change', function () {

        let countDep = departmentTeach.children('option').length;
        let countTch = teacher.children('option').length;

        console.log(countDep);

        if(countDep > 1)
        {
            departmentTeach.empty();
            departmentTeach.append('<option value="0" selected>-----</option>')
        }
        if(countTch > 1)
        {
            teacher.empty();
            teacher.append('<option value="0" selected>-----</option>')
        }

        console.log($(this).val());

        let data_fac = {};
        data_fac.id_faculty = $(this).val();
        data_fac.current_language = selLang.val();

        $.ajax({
            url: '/faculty/',
            type: 'GET',
            data: data_fac,
            cache: true,
            success: function (data) {
                let parseData = JSON.parse(data);
                for (let key in parseData) {
                    departmentTeach.append('<option value="' + key + '">' + parseData[key] + '</option>')
                }
            },
            error: function () {
            }
        })

    }); // обработка изменения факультета преподавателя

    departmentTeach.on('change', function () {

        let countTch = teacher.children('option').length;

        if(countTch > 1)
        {
            teacher.empty();
            teacher.append('<option value="0" selected>-----</option>')
        }

        console.log($(this).val());

        let data_dep = {};
        data_dep.id_department = $(this).val();
        data_dep.current_language = selLang.val();

        $.ajax({
            url: '/department/',
            type: 'GET',
            data: data_dep,
            cache: true,
            success: function (data) {
                let parseData = JSON.parse(data);
                for (let key in parseData) {
                    teacher.append('<option value="' + key + '">' + parseData[key] + '</option>')
                }
            },
            error: function () {
            }
        })

    }); // обработка изменения кафедры преподавателя

});