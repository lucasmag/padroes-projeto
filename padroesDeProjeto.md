### Questão 7 - Faça uma tabela explicando a utilidade de cada um dos padrões GoF
#

<html>
  <table border="1">
		<tr>
			<th colspan="2"><strong>Padrões de criação</strong></th>
		</tr>
		<tr>
			<td>Abstract Factory</td>
			<td>Este padrão permite a criação de famílias de objetos relacionados ou dependentes por meio de uma única interface e sem que a classe concreta seja especificada. O uso deste padrão torna possível trocar implementações concretas sem alterar o código que estas usam, mesmo em tempo de execução. </td>
		</tr>
		<tr>
			<td>Object Pool</td>
			<td>É um padrão de projeto que usa um conjunto de objetos inicializados mantidos prontos para uso - um "pool" - em vez de alocá-los e destruí-los sob demanda. Um cliente do pool solicitará um objeto do pool e executará operações no objeto retornado. Quando o cliente termina, ele retorna o objeto ao pool, em vez de destruí-lo; isso pode ser feito manualmente ou automaticamente.</td>
		</tr>
		<tr>
			<td>Builder</td>
			<td>O padrão Builder, da forma como foi descrito no livro Design Patterns: Elements of Reusable Object-Oriented Software, contém os seguintes elementos:
				<br><strong>Director</strong> — constrói um objeto utilizando a interface do builder;
				<br><strong>Builder</strong> — especifica uma interface para um construtor de partes do objeto-produto;
				<br><strong>Concrete builder</strong> — define uma implementação da interface builder, mantém a representação que cria e fornece interface para recuperação do produto;
				<br><strong>Product</strong> — o objeto complexo acabado de construir. Inclui classes que definem as partes constituintes.</td>
		</tr>
		<tr>
			<td>Factory</td>
			<td>Factory Method permite às classes delegar para subclasses decidirem, isso é feito através da criação de objetos que chamam o método fabrica especificado numa interface e implementado por um classe filha ou implementado numa classe abstrata e opcionalmente sobrescrito por classes derivadas.</td>
		</tr>
		<tr>
			<td>Prototype</td>
			<td>Prototype, é um criacional que permite a criação de novos objetos a partir de um modelo original ou protótipo que é clonado.</td>
		</tr>
		<tr>
			<td>Singleton</td>
			<td>Este padrão garante a existência de apenas uma instância de uma classe, mantendo um ponto global de acesso ao seu objeto.</td>
		</tr>
		<tr>
			<th colspan="2"><strong>Padrões estruturais</strong></th>
		</tr>
		<tr>
			<td>Private Class</td>
			<td>Os dados de classe privada são um padrão de design na programação de computadores usados ​​para encapsular os atributos de classe e sua manipulação.</td>
		</tr>
		<tr>
			<td>Adapter</td>
			<td>Adapter converte a interface de uma classe para outra interface que o cliente espera encontrar, "traduzindo" solicitações do formato requerido pelo usuário para o formato compatível com o a classe adaptee e as redirecionando. Dessa forma, o Adaptador permite que classes com interfaces incompatíveis trabalhem juntas.</td>
		</tr>
		<tr>
			<td>Bridge</td>
			<td>Bridge é um padrão de projeto de software utilizado quando é desejável que uma interface (abstração) possa variar independentemente das suas implementações.</td>
		</tr>
		<tr>
			<td>Composite</td>
			<td>Composite um padrão de projeto de software utilizado para representar um objeto formado pela composição de objetos similares. Este conjunto de objetos pressupõe uma mesma hierarquia de classes a que ele pertence. Tal padrão é, normalmente, utilizado para representar listas recorrentes - ou recursivas - de elementos. Além disso, este modo de representação hierárquica de classes permite que os elementos contidos em um objeto composto sejam tratados como se fossem um objeto único. Desta forma, os métodos comuns às classes podem ser aplicados, também, ao conjunto agrupado no objeto composto.</td>
		</tr>
		<tr>
			<td>Decorator</td>
			<td>Decorator é um padrão de projeto de software que permite adicionar um comportamento a um objeto já existente em tempo de execução, ou seja, agrega dinamicamente responsabilidades adicionais a um objeto. Decorators oferecem uma alternativa flexível ao uso de herança para estender uma funcionalidade, com isso adiciona-se uma responsabilidade ao objeto e não à classe.</td>
		</tr>
		<tr>
			<td>Façade</td>
			<td>O Padrão de projeto Façade é um padrão de design de software usado comumente com programação orientada a objetos. Este nome é uma analogia para uma fachada arquitetural. Um Façade é um objeto que provê uma interface simplificada para um corpo de código maior, como por exemplo, uma biblioteca de classes.</td>
		</tr>
		<tr>
			<td>Business delegate</td>
			<td>Business delegate é um padrões de projeto da engenharia de software, utilizado para aplicativos multicamadas. O padrão projeto de Delegação de Negócio do inglês "Business Delegate" é usado para separar a camada de apresentação/externa das regras/lógicas de negócio. A razão para utilizar essa abordagem é reduzir o acoplamento entre as camadas, porque o alto acoplamento pode causar vários problemas no projeto, recomendado na Java EE como padrão de projeto.</td>
		</tr>
		<tr>
			<td>Flyweight</td>
			<td>Flyweight é um padrão de projeto de software apropriado quando vários objetos devem ser manipulados em memória sendo que muitos deles possuem informações repetidas. Dado que o recurso de memória é limitado, é possível segregar a informação repetida em um objeto adicional que atenda as características de imutabilidade e comparabilidade (que consiga ser comparado com outro objeto para determinar se ambos carregam a mesma informação).</td>
		</tr>
		<tr>
			<td></td>
			<td>O Padrão de Projeto Proxy possui três principais finalidades, sendo elas:
			<li>Prover um substituto ou placeholder para um outro objeto controlar seu acesso.</li>
			<li>Usar um nível extra de indireção para fornecer acesso distribuído, controlado ou inteligente.</li>
			<li>Adicionar um agregador e delegador para proteger o componente real de complexidade indevida</li></td>
					</tr>
		<tr>
		<tr>
			<th colspan="2"><strong>Padrões Comportamentais</strong></th>
		</tr>
			<td>Chain of Responsibility</td>
			<td>Chain of Responsibility é um padrão GOF cuja principal função é evitar a dependência entre um objeto receptor e um objeto solicitante. Consiste em uma série de objetos receptores e de objetos de solicitação, onde cada objetos de solicitação possui uma lógica interna que separa quais são tipos de objetos receptores que podem ser manipulados.</td>
		</tr>
		<tr>
			<td>Command</td>
			<td>Command é um dos 11 padrões comportamentais dentre os 23 padrões de projeto de software do GOF. Na programação orientada a objeto, o command é um padrão no qual um objeto é usado para encapsular toda informação necessária para executar uma ação ou acionar um evento em um momento posterior.</td>
		</tr>
		<tr>
			<td>Interpreter</td>
			<td>Interpreter é um dos padrões de projeto de software, famosos como "Design Patterns", muito utilizado para a resolução de problemas quando a modelagem de sistemas ou softwares. Esse padrão esta incluso na categoria de Padrão Comportamental, ou seja, ele busca solucionar problemas de modelagem que tratam o comportamento de classes.</td>
		</tr>
		<tr>
			<td>Interator</td>
			<td>Um iterador se refere tanto ao objeto que permite ao programador percorrer um container, (uma coleção de elementos) particularmente listas, quanto ao padrão de projetos Iterator, no qual um iterador é usado para percorrer um container e acessar seus elementos. O padrão Iterator desacopla os algoritmos dos recipientes, porém em alguns casos, os algoritmos são necessariamente específicos dos containers e, portanto, não podem ser desacoplados.</td>
		</tr>
		<tr>
			<td>Mediator</td>
			<td>É um padrão de projeto usado frequentemente quando deseja-se encapsular como os objetos interagem, ou seja, a comunicação entre os objetos é estabelecida através do Mediator. Este padrão é considerado um padrão comportamental, pois o padrão pode alterar o comportamento da aplicação (programa).O Mediator promove o fraco acoplamento ao evitar que objetos se referiram uns aos outros explicitamente.</td>
		</tr>
			<td>Memento</td>
			<td>Memento é um padrão de projeto de software documentado no Catálogo Gang of Four, sendo considerado como um padrão comportamental. Ele permite armazenar o estado interno de um objeto em um determinando momento, para que seja possível retorná-lo a este estado, sem que isso cause problemas com o encapsulamento.</td>
		</tr>
		<tr>
			<td>Observer</td>
			<td>O Observer é um padrão de projeto de software que define uma dependência um-para-muitos entre objetos de modo que quando um objeto muda o estado, todos seus dependentes são notificados e atualizados automaticamente. Permite que objetos interessados sejam avisados da mudança de estado ou outros eventos ocorrendo num outro objeto.
			O padrão Observer é também chamado de Publisher-Subscriber, Event Generator e Dependents.</td>
		</tr>
		<tr>
			<td>State</td>
			<td>Permite que um objeto altere seu comportamento de acordo com o estado interno que se encontra em um momento dado.</td>
		</tr>
		<tr>
			<td>Strategy</td>
			<td>Strategy é um padrão de projeto de software, pode ser chamado de policy. Este padrão foi documentado no Catálogo GOF (Gang of Four), sendo categorizado como um padrão comportamental de desenvolvimento de software.  De modo que delega as responsabilidades adquiridas pelas entidades, atribuindo, portanto, o comportamento. Assim a comunicação entre os objetos é aprimorada, pois há a distribuição das responsabilidades.</td>
		</tr>
		<tr>
			<td>Template Method</td>
			<td>Um Template Method auxilia na definição de um algoritmo com partes do mesmo definidos por métodos abstratos. As subclasses devem se responsabilizar por estas partes abstratas, deste algoritmo, que serão implementadas, possivelmente de várias formas, ou seja, cada subclasse irá implementar à sua necessidade e oferecer um comportamento concreto construindo todo o algoritmo.</td>
		</tr>
		<tr>
			<td>Visitor Pattern</td>
			<td> O visitor pattern é um padrão de projeto comportamental. Representa uma operação a ser realizada sobre elementos da estrutura de um objeto. O Visitor permite que se crie uma nova operação sem que se mude a classe dos elementos sobre as quais ela opera. É uma maneira de separar um algoritmo da estrutura de um objeto. Um resultado prático é a habilidade de adicionar novas funcionalidades a estruturas de um objeto pré-existente sem a necessidade de modificá-las.</td>
		</tr>
  </table>
</html>

### Questão 8 -  Idem para GRASP
#

<html>
  <body>
    <table border="1">
      <tr>
        <th colspan="2"><strong>Padrões de GRASP</strong></th>
      </tr>
      <tr>
        <td>Controller</td>
        <td>O padrão controlador atribui a responsabilidade de manipular eventos do sistema para uma classe que não seja de interface do usuário (UI) que representa o cenário global ou cenário de caso de uso. Um objeto controlador é um objeto de interface não-usuário, responsável por receber ou manipular um evento do sistema. </td>
      </tr>
      <tr>
        <td>Creator</td>
        <td>A criação de objetos é uma das mais comuns atividades em um sistema orientado a objetos. Descobrir qual classe é responsável por criar objetos é uma propriedade fundamental da relação entre objetos de classes particulares.
          <br>Em geral, uma classe B deve ser responsável por criar instâncias de classe A se uma, ou preferencialmente mais, das seguintes afirmações se aplicam:
          <br><li>Instâncias de B contêm ou agregam instâncias de A;</li>
          <br><li>Instâncias de B gravam instâncias de A;</li>
          <br><li>Instâncias de B utilizam de perto instâncias de A;</li>
          <br><li>Instâncias de B têm as informações de iniciação das instâncias de A e passam isso na criação.</li></td>
      </tr>
      <tr>
        <td>Information expert</td>
        <td>Especialista na informação é um princípio utilizado para determinar onde delegar responsabilidades. Essas responsabilidades incluem métodos, campos computados, e assim em diante.
          Usando o princípio information expert, uma abordagem geral para atribuir responsabilidades é olhar para uma determinada responsabilidade, determinar a informação necessária para cumpri-la e depois determinar onde essa informação está armazenada.	
          Information expert guia a colocará a responsabilidade na classe com a maioria das informações necessárias para cumpri-la.</td>
      </tr>
      <tr>
        <td>Indirection</td>
        <td>O padrão de indireção suporta baixo acoplamento (e potencial de reutilização) entre dois elementos, atribuindo a objeto intermediário a responsabilidade de ser o mediador entre eles. Um exemplo é a introdução do componente controlador para mediação entre dados (modelo) e sua representação (visualização) no padrão MVC.</td>
      </tr>
      <tr>
        <td>Alta coesão</td>
        <td>Alta coesão é um padrão avaliativo que tenta manter os objetos adequadamente focados, gerenciáveis e compreensíveis. A alta coesão é geralmente utilizada em suporte de baixo acoplamento. A alta coesão significa que as responsabilidades de um determinado elemento estão fortemente relacionadas e altamente focadas. A quebra de programas em classes e subsistemas é um exemplo de atividades que aumentam as propriedades coesivas de um sistema. Alternativamente, a baixa coesão é uma situação em que um determinado elemento tem muitas responsabilidades distintas, não relacionadas. Elementos com baixa coesão muitas vezes sofrem de ser difíceis de entender, reutilizar, manter e são avessos à mudança.</td>
      </tr>
      <tr>
        <td>Baixo acoplamento</td>
        <td>O acoplamento é uma medida de quão forte um elemento está conectado, tem conhecimento ou depende de outros elementos. O baixo acoplamento é um padrão de avaliação que determina como atribuir responsabilidades de suporte:
          <br><li>Menor dependência entre as classes,</li>
          <br><li>Mudança em uma classe com menor impacto em outras,</li>
          <br><li>Maior potencial de reutilização.</td></li>
      </tr>
      <tr>
        <td>Polimorfismo</td>
        <td>De acordo com o princípio do polimorfismo, a responsabilidade de definir a variação dos comportamentos com base no tipo é atribuída ao tipo para o qual essa variação ocorre. Isto é conseguido utilizando operações polimórficas. O usuário do tipo deve usar operações polimórficas em vez de ramificações explícitas com base no tipo.</td>
      </tr>
      <tr>
        <td>Pure fabrication</td>
        <td>Uma fabricação/invenção pura é uma classe artificial que não representa um conceito no domínio do problema, especialmente feito para conseguir baixo acoplamento, alta coesão e o potencial de reutilização derivado (quando uma solução apresentada pelo padrão information expert não é). Esse tipo de classe é chamado de "serviço" em padrão orientado a domínio.</td>
      </tr>
      <tr>
        <td>Protected variations</td>
        <td>O padrão variações protegidas protege elementos das variações em outros elementos (objetos, sistemas, subsistemas) envolvendo o foco de instabilidade com uma interface e usando polimorfismo para criar várias implementações desta interface.</td>
      </tr>
    </table>
  </body>
</html>
