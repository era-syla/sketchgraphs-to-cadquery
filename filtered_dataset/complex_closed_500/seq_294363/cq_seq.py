import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.01905, 1.11714).lineTo(-0.01905, 1.11714).lineTo(-0.01905, 1.14254).lineTo(0.01905, 1.14254).lineTo(0.01905, 1.11714).close()
solid=wp_sketch0.add(loop0).extrude(0.08785546465959747)
