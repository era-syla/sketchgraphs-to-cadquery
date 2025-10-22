import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.02507, 0.02228).threePointArc((0.01761, 0.03136), (0.00587, 0.0319)).threePointArc((0.01161, 0.01939), (0.02507, 0.02228)).close()
solid=wp_sketch0.add(loop0).extrude(0.05347384717510023)
