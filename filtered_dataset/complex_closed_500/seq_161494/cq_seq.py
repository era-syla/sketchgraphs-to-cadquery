import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.06292, 0.06039).lineTo(-0.04717, 0.02633).lineTo(-0.02928, 0.02633).lineTo(-0.00962, 0.04996).lineTo(0.04118, 0.04996).lineTo(0.01511, 0.06851).lineTo(-0.01669, 0.06851).lineTo(-0.04386, 0.06851).lineTo(-0.06292, 0.06039).close()
solid=wp_sketch0.add(loop0).extrude(0.21934471658417187)
