import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.01905, -0.37465).lineTo(1.27, -0.37465).lineTo(1.27, -0.83185).lineTo(-0.01905, -0.83185).lineTo(-0.01905, -0.37465).close()
solid=wp_sketch0.add(loop0).extrude(2.340671886296431)
