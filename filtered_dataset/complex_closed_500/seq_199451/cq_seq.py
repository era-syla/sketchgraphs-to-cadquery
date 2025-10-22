import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0762, 0.0).lineTo(0.0762, 0.01905).lineTo(0.05662, 0.01905).lineTo(0.05662, 0.04445).lineTo(0.0762, 0.04445).lineTo(0.0762, 0.0635).lineTo(0.0, 0.0635).lineTo(0.0, 0.04445).lineTo(0.02421, 0.04445).lineTo(0.02421, 0.01905).lineTo(0.0, 0.01905).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.1885546922440084)
