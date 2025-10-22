import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.02586, 0.0265).lineTo(0.05627, 0.0265).lineTo(0.05627, -0.0265).lineTo(0.02586, -0.0265).lineTo(0.02586, 0.0265).close()
solid=wp_sketch0.add(loop0).extrude(-0.06893876817927673)
