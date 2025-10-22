import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00325, -0.00325).lineTo(-0.00325, -0.00325).lineTo(-0.00325, 0.00325).lineTo(0.00325, 0.00325).lineTo(0.00325, -0.00325).close()
solid=wp_sketch0.add(loop0).extrude(-0.00038062009609702115)
