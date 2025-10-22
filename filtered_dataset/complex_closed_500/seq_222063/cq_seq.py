import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.10564, 0.04091).lineTo(-0.03564, 0.04091).lineTo(-0.03564, 0.06091).lineTo(-0.10564, 0.06091).lineTo(-0.10564, 0.04091).close()
solid=wp_sketch0.add(loop0).extrude(-0.008563187531549884)
