import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.025, -0.0011).lineTo(0.015, -0.0011).lineTo(0.015, 0.0024).lineTo(0.025, 0.0024).lineTo(0.025, -0.0011).close()
solid=wp_sketch0.add(loop0).extrude(0.0172170576980467)
