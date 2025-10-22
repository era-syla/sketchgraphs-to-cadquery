import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00854, 0.04099).lineTo(0.00854, 0.03099).lineTo(0.01511, 0.03099).threePointArc((0.01582, 0.03069), (0.01611, 0.02999)).lineTo(0.01611, -0.05451).lineTo(0.01943, -0.05451).lineTo(0.01943, 0.03849).threePointArc((0.01869, 0.04026), (0.01693, 0.04099)).lineTo(0.00854, 0.04099).close()
solid=wp_sketch0.add(loop0).extrude(0.10248525265836386)
