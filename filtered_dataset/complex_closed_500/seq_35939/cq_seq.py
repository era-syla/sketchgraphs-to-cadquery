import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.025, 0.02641).lineTo(0.024, 0.02641).lineTo(0.024, 0.03441).lineTo(0.025, 0.03441).lineTo(0.025, 0.02641).close()
solid=wp_sketch0.add(loop0).extrude(-0.004433639739725239)
