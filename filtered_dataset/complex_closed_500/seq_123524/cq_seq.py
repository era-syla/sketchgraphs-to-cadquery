import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00171, 0.0094).threePointArc((-0.0, 0.01111), (0.00171, 0.0094)).lineTo(0.00171, 0.00622).threePointArc((0.0, 0.00451), (-0.00171, 0.00622)).lineTo(-0.00171, 0.0094).close()
solid=wp_sketch0.add(loop0).extrude(-0.014863657115088596)
