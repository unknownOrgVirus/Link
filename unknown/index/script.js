console.clear();

// const loginBtn = document.getElementById('login');
// const signupBtn = document.getElementById('signup');

loginBtn.addEventListener('click', (e) => {
	let parent = e.target.parentNode.parentNode;
	Array.from(e.target.parentNode.parentNode.classList).find((element) => {
		if(element !== "slide-up") {
			parent.classList.add('slide-up')
		}else{
			signupBtn.parentNode.classList.add('slide-up')
			parent.classList.remove('slide-up')
		}
	});
});

signupBtn.addEventListener('click', (e) => {
	let parent = e.target.parentNode;
	Array.from(e.target.parentNode.classList).find((element) => {
		if(element !== "slide-up") {
			parent.classList.add('slide-up')
		}else{
			loginBtn.parentNode.parentNode.classList.add('slide-up')
			parent.classList.remove('slide-up')
		}
	});
});

function GoSweetAlert(icon ,title ,text) {
	Swal.fire({
		icon: icon,
		title: title,
		text: text,
		footer: '',
		confirmButtonText: 'OK !',
		confirmButtonColor: 'green',
		didClose: true,
	});
}

if (window.XMLHttpRequest) {
    httpRequest = new XMLHttpRequest();
} else if (window.ActiveXObject) {
    httpRequest = new ActiveXObject("Microsoft.XMLHTTP");
}
function Send(word = document.getElementsByClassName("submit-btn").value){
			GoSweetAlert('success','TNT :)','Click OK to continue');
}