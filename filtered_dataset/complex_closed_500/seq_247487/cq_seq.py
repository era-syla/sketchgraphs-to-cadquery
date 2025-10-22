import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00615, -0.0162).lineTo(-0.00615, -0.0162).lineTo(-0.00615, 0.0162).lineTo(0.00615, 0.0162).lineTo(0.00615, -0.0162).close()
solid=wp_sketch0.add(loop0).extrude(-0.0028676975526317496)
