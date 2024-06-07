import { } from 'react';
import '../css/style.scss';
import wave from '../assets/wavetr.jpeg';

function Home() {
    return (
        <>
            <section id='home'>
                <h1 className='title'>Ocean Tracking</h1>
                <img src="" alt="" />
            </section>
            <section>
                <div className="card-group p-5">
                    <div className="card">

                        <div className="card-body">
                            <h5 className="card-title">Tecnologia</h5>
                            <p className="card-text">solução inovadora para o monitoramento ambiental marinho, utilizando boias derivantes equipadas com sensores avançados. Essas boias autônomas são capazes de medir parâmetros críticos como pH e temperatura da água, transmitindo dados em tempo real através de conectividade Wi-Fi.
                            </p>
                            <img src="" alt="" />
                        </div>
                    </div>
                    <div className="card">

                        <div className="card-body">
                            <h5 className="card-title">Conectividade</h5>
                            <p className="card-text">Graças a conexção Wi-Fi, podemos monitorar a localização das bóias e receber dados instantaneamente, permitindo um acompanhamento contínuo e preciso das condições oceânicas.</p>
                            <img src="" alt="" />
                        </div>
                    </div>
                    <div className="card">

                        <div className="card-body">
                            <h5 className="card-title">Sustentabilidade</h5>
                            <p className="card-text">As boias utilizam energia solar para operar, garantindo uma solução ecologicamente correta e de longo prazo.</p>
                            <img src="" alt="" />
                        </div>
                    </div>
                </div>
            </section>
            <section className='container white'>
                <p>O monitoramento ambiental dos oceanos é uma questão de crescente importância, tanto para a preservação dos ecossistemas marinhos quanto para o avanço da pesquisa científica. Estudos recentes indicam que os oceanos absorvem cerca de 30% do dióxido de carbono (CO₂) produzido pela atividade humana, desempenhando um papel crucial na regulação do clima global. No entanto, a qualidade da água e a saúde dos ecossistemas marinhos estão cada vez mais ameaçadas por fatores como poluição, acidificação e mudanças climáticas.</p>
                <p>Segundo a Organização das Nações Unidas (ONU), aproximadamente 80% da poluição marinha provém de atividades terrestres, resultando em uma quantidade significativa de resíduos e produtos químicos que acabam nos oceanos. Além disso, a acidificação dos oceanos, causada pelo aumento das concentrações de CO₂, está alterando a química da água, impactando negativamente a vida marinha. Dados do Painel Intergovernamental sobre Mudanças Climáticas (IPCC) mostram que o pH da superfície dos oceanos já diminuiu em cerca de 0,1 unidade desde a era pré-industrial, representando um aumento de 26% na acidez.
                </p>
                <p>Para enfrentar esses desafios, é essencial dispor de sistemas de monitoramento ambiental que sejam precisos, eficientes e capazes de operar em tempo real. Métodos tradicionais de coleta de dados marinhos, como embarcações de pesquisa e estações fixas, são muitas vezes limitados em alcance e custo-efetividade. Em contrapartida, tecnologias emergentes oferecem novas possibilidades para melhorar a qualidade e a quantidade de dados ambientais coletados.
                </p>
            </section>
            <section className='container display-center p-3 video'>
                <iframe className='video-frame' src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAGHNjQ82NI&#x2F;cSN1_mJUAOgSTlXPrxpH8A&#x2F;watch?embed"></iframe>
            </section>
            <section className='container'>
                <img src={wave} />
            </section>
        </>
    )
}
export default Home;