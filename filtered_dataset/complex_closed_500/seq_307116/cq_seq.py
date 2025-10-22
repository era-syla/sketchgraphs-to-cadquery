import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.05122, -0.01815).lineTo(-0.01157, -0.01815).lineTo(-0.01157, 0.07232).lineTo(-0.05122, 0.07232).lineTo(-0.05122, -0.01815).close()
solid=wp_sketch0.add(loop0).extrude(0.13028248423890942)
