import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.02542, 0.02542).lineTo(-0.02542, 0.02542).lineTo(-0.02542, -0.02542).lineTo(0.02542, -0.02542).lineTo(0.02542, 0.02542).close()
solid=wp_sketch0.add(loop0).extrude(0.06755283841804777)
