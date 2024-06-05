import err from '../assets/error.png'
import '../css/style.scss';
function Error() {
  return (
  <>
  <section className="error">
    <h1>404-Página não encontrada !!!</h1>
    <img src={err} alt="ERRO" />
  </section>
  
  </>
  )
}
export default Error;