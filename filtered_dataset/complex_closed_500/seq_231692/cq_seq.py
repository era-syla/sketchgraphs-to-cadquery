import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(1.2381, 18.51993).lineTo(-1.0219, 18.51993).lineTo(-1.0219, 13.97785).lineTo(1.2381, 13.97785).lineTo(1.2381, 18.51993).close()
solid=wp_sketch0.add(loop0).extrude(-11.41391609051975)
