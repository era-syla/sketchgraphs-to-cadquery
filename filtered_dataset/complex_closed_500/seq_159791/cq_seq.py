import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.033, -0.0265).lineTo(-0.033, -0.0265).lineTo(-0.033, -0.0285).lineTo(0.033, -0.0285).lineTo(0.033, -0.0265).close()
solid=wp_sketch0.add(loop0).extrude(0.129397638229716)
