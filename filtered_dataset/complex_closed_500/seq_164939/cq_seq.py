import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.016, 0.016).lineTo(0.016, 0.016).lineTo(0.016, -0.016).lineTo(-0.016, -0.016).lineTo(-0.016, 0.016).close()
solid=wp_sketch0.add(loop0).extrude(0.04220251313747406)
