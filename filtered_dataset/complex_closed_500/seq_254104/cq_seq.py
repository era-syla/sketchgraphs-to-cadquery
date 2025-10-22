import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(-0.12, 0.0).lineTo(-0.12, -0.005).lineTo(-0.116, -0.005).lineTo(-0.116, -0.008).lineTo(-0.127, -0.008).lineTo(-0.127, -0.015).lineTo(-0.009, -0.015).lineTo(-0.009, -0.008).lineTo(0.004, -0.008).lineTo(0.004, -0.005).lineTo(0.0, -0.005).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.3220118240875098)
