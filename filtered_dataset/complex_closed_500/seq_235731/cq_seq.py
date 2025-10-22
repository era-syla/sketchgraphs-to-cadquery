import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-10.9728, 3.81).lineTo(-10.8204, 3.81).lineTo(-10.8204, 2.1845).lineTo(-10.9728, 2.1845).lineTo(-10.9728, 3.81).close()
solid=wp_sketch0.add(loop0).extrude(-0.9051952484498383)
