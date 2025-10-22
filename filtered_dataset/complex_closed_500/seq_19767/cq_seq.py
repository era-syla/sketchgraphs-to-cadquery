import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0075, -0.0105).lineTo(-0.0075, -0.0105).lineTo(-0.0075, 0.0105).lineTo(0.0075, 0.0105).lineTo(0.0075, -0.0105).close()
solid=wp_sketch0.add(loop0).extrude(0.025806521953577865)
