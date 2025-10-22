import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.082, -0.0065).lineTo(-0.14592, -0.0065).lineTo(-0.14592, -0.03567).lineTo(-0.082, -0.03567).lineTo(-0.082, -0.0065).close()
solid=wp_sketch0.add(loop0).extrude(-0.1047302521090722)
