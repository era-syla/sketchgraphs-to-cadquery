import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.045, 0.395).lineTo(0.12, 0.395).lineTo(0.12, 0.47).lineTo(0.045, 0.47).lineTo(0.045, 0.395).close()
solid=wp_sketch0.add(loop0).extrude(0.20187000701385277)
