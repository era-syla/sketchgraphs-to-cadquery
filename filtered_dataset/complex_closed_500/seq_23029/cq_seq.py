import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.89, 0.95).lineTo(3.475, 0.95).lineTo(3.475, 0.0).lineTo(0.89, 0.0).lineTo(0.89, 0.95).close()
solid=wp_sketch0.add(loop0).extrude(0.24164479424643495)
