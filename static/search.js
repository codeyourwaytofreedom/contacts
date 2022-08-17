
const checkbox_dep = document.getElementById("dep");
const checkbox_name = document.getElementById("name");
const search_box = document.querySelector(".search_box");


checkbox_dep.addEventListener('change', check_dep)
checkbox_name.addEventListener('change', check_name)


function check_dep()
{
  if (this.checked) {
    console.log("Checkbox is checked..");
    checkbox_name.checked = false;
    search_box.placeholder = "search by department";

  }
}

function check_name()
{
  if (this.checked) {
    console.log("Checkbox is checked..");
    checkbox_dep.checked = false;
    search_box.placeholder = "search by employee";
  }
}