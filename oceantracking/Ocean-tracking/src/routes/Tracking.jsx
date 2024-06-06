import React, { useState, useEffect } from 'react';
import '../css/style.scss';

function Tracking() {
    const [boias, setBoia] = useState([]);

    useEffect(() => {
        console.log("Fazendo requisição para o endpoint /api/data");
        fetch("http://127.0.0.1:5000/?page=0")
            .then((resp) => {
                console.log("Resposta recebida", resp);
                return resp.json();
            })
            .then((data) => {
                console.log("Dados recebidos:", data);
                setBoia(data);
            })
            .catch((error) => {
                console.error("Erro ao buscar dados:", error);
            });
    }, []);

    return (
        <>
            <section>
                <h1 className='white'>Dados do Oceano</h1>
            </section>
            <section>
                <table className="table table-striped table-dark">
                    <thead>
                        <tr>
                            <th scope="col">Data</th>
                            <th scope="col">Impurezas</th>
                            <th scope="col">Latitude</th>
                            <th scope="col">Longitude</th>
                            <th scope="col">Temp.Água</th>
                            <th scope="col">Temp.Amb</th>
                            <th scope="col">Turbidez</th>
                            <th scope="col">Umidade</th>
                        </tr>
                    </thead>
                    <tbody>
                        {boias.map((item, indice) => (
                            <tr key={indice}>
                                <td>{item.data}</td>
                                <td>{item.impurezas}</td>
                                <td>{item.latitude}</td>
                                <td>{item.longitude}</td>
                                <td>{item.temperatura_agua}</td>
                                <td>{item.temperatura_ambiente}</td>
                                <td>{item.turbidez}</td>
                                <td>{item.umidade}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </section>
        </>
    );
}

export default Tracking;
