$(document).ready(() => {

    getFileList()
    getReportList()

    $("ul.tabs").tabs("div.panels > div");

    $("#tab_suites_div").click(getFileList)
    $("#tab_reports_div").click(getReportList)


    $("#toRunTestCases").click((e) => {
        e.preventDefault()
        $('body').loading({
            message: "running..."
        });
        fetch("server/trunhtml")
            .then(response => response.text())
            .then(t => $('body').loading({
                shownClass: "div-text",
                hiddenClass: "div-text",
                message: "<div class='console'>" + t.replace(/\\n/g, "<br/>").replace(/'b'/g, "") + "</div>",
                stoppable: true
            }))
    })
    $("#toUpdateTestCases").click((e) => {
        e.preventDefault()
        toastr.success('OK')
        fetch("server/update")
            .then(response => response.text())

    })

    $('#simple-menu').sidr();

    $('#sms-a').click();


    $('#sql-table-button').click(getSms);


})

function getSms() {
     Table().init({
                id: 'sql-table-div',
                header: [],
                data: []
            });
    fetch("sms/list")
        .then(response => response.json())
        .then((json) => {
            let header = Object.keys(json[0])
            let data = json.map(t => Object.values(t))

            Table().init({
                id: 'sql-table-div',
                header: header,
                data: data
            });
            $("#sql-table-div td:nth-child(3)").each(function (index, item) {
                $(this).html("<div class='tip-bco'><span title='" + $(item).text() + "'>" + $(item).text() + "</span></div>")
            })
            $("#sql-table-div td:nth-child(3) span").tooltipster()
            // $("#sql-table-div td:nth-child(3) span").tooltip({effect: 'fade', fadeOutSpeed: 200000000, offset: [-50, -80], })
        })
}

function getFileList() {
    fetch("suites/list?")
        .then(response => response.json())
        .then((json) => {
            let html = json.reduce((total, currentValue) => total += `<div class="div-line">
                    <button class="icono-play button-mini" onclick='runPytestAFile("${currentValue}")'></button>
                    <span class="over-hidden">run</span>
                    <a class="file-link" href='${currentValue}'>${currentValue}</a>
                    <span class="over-hidden-open">open</span>
                    <span class="img-box-out"><a class="img-box" href="${parsePng(currentValue)}"><img  class="img-box-in" src="${parsePng(currentValue)}"/></a></span>

                    </div>`, "")
            $("#suites_div").html(html)
            $(".img-box").imgbox({speedIn: 200, speedOut: 500});
        })
}

function getReportList() {
    fetch("report/list?")
        .then(response => response.json())
        .then((json) => {
            let html = json.reduce((total, currentValue) => total += `<div class="div-line">
                    <button class="icono-sitemap button-mini" onclick='parseJunitFile("${currentValue}")'></button>
                    <span class="over-hidden">view</span>
                    <a class="file-link" href='Reports/${currentValue}'>${currentValue}</a>
                    <span class="over-hidden-open">open</span>            
            </div>`, "")
            $("#report_div").html(html)
        })
}

function parseJunitFile(file) {

}

function parsePng(src) {
    if (src == null) return null
    src = src.replace(/\/\//g, "/")
    src = src.replace(/\.py$/, ".png")
    return src
}

function runPytestAFile(file) {
    $('body').loading({
        message: "running...",
        stoppable: true

    });
    fetch("server/runfile?file=" + file)
        .then(response => {
            $('body').loading({
                message: response.status,
                stoppable: true
            })
            return response.text()
        })
        .then(t => $('body').loading({
            shownClass: "div-text",
            hiddenClass: "div-text",
            message: "<div class='console'>" + t.replace(/\\n/g, "<br/>").replace(/'b'/g, "") + "</div>",
            stoppable: true
        }))
}


toastr.options = {
    "closeButton": false,
    "debug": false,
    "newestOnTop": false,
    "progressBar": false,
    "positionClass": "toast-top-center",
    "preventDuplicates": false,
    "onclick": null,
    "showDuration": "300",
    "hideDuration": "1000",
    "timeOut": "2",
    "extendedTimeOut": "1000",
    "showEasing": "swing",
    "hideEasing": "linear",
    "showMethod": "fadeIn",
    "hideMethod": "fadeOut"
}

