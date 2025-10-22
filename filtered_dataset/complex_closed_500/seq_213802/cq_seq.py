import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.02643, -0.0127).lineTo(0.02643, -0.0381).lineTo(-0.07517, -0.0381).lineTo(-0.07517, 0.0127).lineTo(0.02643, -0.0127).close()
solid=wp_sketch0.add(loop0).extrude(-0.0961821728438338)
