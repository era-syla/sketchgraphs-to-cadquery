import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.01022, 0.02019).lineTo(-0.01046, 0.02019).lineTo(-0.01046, 0.00789).lineTo(0.01022, 0.00789).lineTo(0.01022, 0.02019).close()
solid=wp_sketch0.add(loop0).extrude(-0.03130835470267801)
