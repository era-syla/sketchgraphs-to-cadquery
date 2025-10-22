import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0067, -0.0108).lineTo(0.0067, -0.0108).lineTo(0.0067, 0.0108).lineTo(-0.0067, 0.0108).lineTo(-0.0067, -0.0108).close()
solid=wp_sketch0.add(loop0).extrude(-0.04250204927825452)
