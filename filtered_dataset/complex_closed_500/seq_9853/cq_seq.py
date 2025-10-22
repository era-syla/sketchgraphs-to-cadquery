import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.1016, 0.1016).lineTo(0.1016, 0.1016).lineTo(0.1016, -0.1016).lineTo(-0.1016, -0.1016).lineTo(-0.1016, 0.1016).close()
solid=wp_sketch0.add(loop0).extrude(0.5114953066986293)
