import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.1, 0.05).lineTo(0.1, 0.05).lineTo(0.1, -0.05).lineTo(-0.1, -0.05).lineTo(-0.1, 0.05).close()
solid=wp_sketch0.add(loop0).extrude(0.050222489035815165)
