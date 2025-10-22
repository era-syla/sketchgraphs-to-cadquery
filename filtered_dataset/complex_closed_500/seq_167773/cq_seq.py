import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, 0.03).lineTo(0.08, 0.03).lineTo(0.08, 0.005).lineTo(0.095, 0.005).lineTo(0.095, 0.0).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.16210841102985274)
