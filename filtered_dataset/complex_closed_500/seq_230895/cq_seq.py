import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.29942, 4.48479).lineTo(-0.10698, 4.48479).lineTo(-0.10698, 3.90059).lineTo(0.29942, 3.90059).lineTo(0.29942, 4.48479).close()
solid=wp_sketch0.add(loop0).extrude(-1.3634194675025433)
