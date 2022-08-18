
const checkbox_dep = document.getElementById("dep");
const checkbox_name = document.getElementById("name");
const search_box = document.querySelector(".search_box");


checkbox_dep.addEventListener('change', check_dep)
checkbox_name.addEventListener('change', check_name)
search_box.addEventListener('keydown', submit_check)

function check_dep()
{
  if (this.checked) {
    checkbox_name.checked = false;
    search_box.placeholder = "search by department";
    console.log(search_box.value.length);


  }
}

function check_name()
{
  if (this.checked) {
    checkbox_dep.checked = false;
    search_box.placeholder = "search by employee";
    console.log(search_box.value.length);
  }
}

function submit_check(e) {
                            if (this.value.length<3 && e.code=="Enter" || e.code=="NumpadEnter")
                            {  e.preventDefault();  }
                        }