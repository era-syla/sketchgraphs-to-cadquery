import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0, 0.1).lineTo(-0.002, 0.085).lineTo(-0.017, 0.083).lineTo(-0.002, 0.081).lineTo(-0.0, 0.066).lineTo(0.002, 0.081).lineTo(0.017, 0.083).lineTo(0.002, 0.085).lineTo(-0.0, 0.1).close()
solid=wp_sketch0.add(loop0).extrude(-0.09254820969382319)
