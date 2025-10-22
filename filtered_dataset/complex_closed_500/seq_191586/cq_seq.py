import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0282, -0.028).lineTo(-0.0357, -0.028).lineTo(-0.0357, -0.0295).lineTo(-0.0282, -0.0295).lineTo(-0.0282, -0.028).close()
solid=wp_sketch0.add(loop0).extrude(0.0017141317528902495)
