import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.02064, 0.0).lineTo(0.01413, 0.0).lineTo(0.01413, 0.004).lineTo(0.02064, 0.004).lineTo(0.02064, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.016455829233288265)
