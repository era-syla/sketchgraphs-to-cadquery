import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.01114, 0.09658).lineTo(0.13886, 0.09658).lineTo(0.13886, -0.05342).lineTo(-0.01114, -0.05342).lineTo(-0.01114, 0.09658).close()
solid=wp_sketch0.add(loop0).extrude(-0.4050484894076238)
