import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.008).lineTo(0.009, 0.008).lineTo(0.009, 0.068).lineTo(-0.0, 0.068).lineTo(0.0, 0.008).close()
solid=wp_sketch0.add(loop0).extrude(0.031829568837615965)
