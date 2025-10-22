import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.62, -0.325).lineTo(0.3025, -0.325).lineTo(0.3025, 0.0).lineTo(0.62, 0.0).lineTo(0.62, -0.325).close()
solid=wp_sketch0.add(loop0).extrude(-0.3409788945609188)
