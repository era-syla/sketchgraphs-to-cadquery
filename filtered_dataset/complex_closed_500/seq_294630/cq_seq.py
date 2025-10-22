import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00605, -0.01183).lineTo(0.00605, -0.01183).lineTo(0.00605, 0.01182).lineTo(-0.00605, 0.01182).lineTo(-0.00605, -0.01183).close()
solid=wp_sketch0.add(loop0).extrude(0.03777972742155166)
