import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00425, 0.01).lineTo(-0.00664, 0.01658).lineTo(-0.012, 0.01658).lineTo(-0.012, 0.03158).lineTo(0.012, 0.03158).lineTo(0.012, 0.01658).lineTo(0.00664, 0.01658).lineTo(0.00425, 0.01).lineTo(-0.00425, 0.01).close()
solid=wp_sketch0.add(loop0).extrude(0.020243053302978823)
