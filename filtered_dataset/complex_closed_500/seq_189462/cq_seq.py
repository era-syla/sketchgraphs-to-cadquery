import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0045, -0.024).lineTo(0.0235, -0.024).lineTo(0.0235, 0.01).lineTo(0.0045, 0.01).lineTo(0.0045, -0.024).close()
solid=wp_sketch0.add(loop0).extrude(0.0148403388871208)
