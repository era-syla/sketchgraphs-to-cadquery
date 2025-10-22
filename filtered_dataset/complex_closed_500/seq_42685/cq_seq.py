import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.06657, 0.06879).lineTo(0.09855, 0.06879).lineTo(0.09855, 0.0).lineTo(0.06657, 0.0).lineTo(0.06657, 0.06879).close()
solid=wp_sketch0.add(loop0).extrude(0.20592188099294906)
