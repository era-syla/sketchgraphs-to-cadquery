import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.1, 0.0).lineTo(0.1012, 0.00011).lineTo(0.09352, 0.00236).lineTo(0.08152, 0.00236).lineTo(0.08152, 0.00136).lineTo(0.08052, 0.00136).lineTo(0.08052, 0.00236).lineTo(0.04052, 0.00236).lineTo(0.04052, 0.00136).lineTo(0.03952, 0.00136).lineTo(0.03952, 0.00236).lineTo(0.02452, 0.00236).lineTo(0.02, 0.0045).lineTo(0.0, 0.0045).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.20770332482953632)
