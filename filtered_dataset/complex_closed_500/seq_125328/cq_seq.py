import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0856, 0.01).lineTo(-0.0796, 0.01).lineTo(-0.0796, 0.02524).lineTo(-0.0856, 0.02524).lineTo(-0.0856, 0.01).close()
solid=wp_sketch0.add(loop0).extrude(-0.020567057955435973)
