import { } from 'react';
import '../css/style.scss';

function Home() {
    return (
        <>
            <section id='home'>
                <h1>Ocean Tracking</h1>
            </section>
            <section>
                <h2>Nós</h2>
                <div class="container text-center">
                    <div class="row align-items-start">
                        <div class="col">
                            Tecnologia
                        </div>
                        <div class="col">
                            Conectividade
                        </div>
                        <div class="col">
                            Sustentabilidade
                        </div>
                    </div>
                </div>
            </section>
        </>
    )
}
export default Home;